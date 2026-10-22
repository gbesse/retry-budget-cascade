from .common import integer,identifier,unique_ids

def run(data):
    services=data['services'];ids=set(unique_ids(services));by={s['id']:s for s in services};root=data['root'];requests=integer(data.get('requests',1),1,10**6)
    if root not in ids or len(services)>50:raise ValueError('size_or_root')
    for s in services:
        integer(s['attempts'],1,100);seen=set()
        for call in s.get('calls',[]):
            if call['service'] not in ids or call['service'] in seen:raise ValueError('call')
            seen.add(call['service']);integer(call.get('count',1),1,100)
    visiting=set();memo={}
    def counts(key,retries):
        token=(key,retries)
        if key in visiting:raise ValueError('cycle')
        if token in memo:return memo[token]
        visiting.add(key);s=by[key];attempts=s['attempts'] if retries else 1;out={key:attempts}
        for call in s.get('calls',[]):
            for k,n in counts(call['service'],retries).items():out[k]=out.get(k,0)+attempts*call.get('count',1)*n
        visiting.remove(key);memo[token]=out;return out
    worst={k:v*requests for k,v in counts(root,True).items()};baseline={k:v*requests for k,v in counts(root,False).items()};total=sum(worst.values());base=sum(baseline.values());budget=data.get('shared_budget')
    if budget is not None:integer(budget,0,10**100)
    return {'worst_attempts_by_service':worst,'no_retry_attempts_by_service':baseline,'worst_total_attempts':total,'no_retry_total_attempts':base,'amplification_ratio':total/base,'shared_budget_upper_bound':min(total,budget) if budget is not None else None,'budget_can_exhaust':budget is not None and total>budget,'scope':'nested configured attempts, each parent attempt repeats children; upper bound, not observed requests; shared cap must actually be enforced'}
