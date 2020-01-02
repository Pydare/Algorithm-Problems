def stepPerms(n):
    memo = []
    if n < 0:
        return 0
    if n == 0:
        return 1
    return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)

    def countPathsMemo(n):
        countPathsMemo

    def stepPermsMemo(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] == 0:
        memo[n] = stepPermsMemo(n-1, memo) + stepPermsMemo(n-2,memo) + stepPermsMemo(n-3,memo)
    
