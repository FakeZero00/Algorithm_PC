import random

random.seed(20251201)
BIN_SIZE = 100

def fits(bin, obj):
    if not bin: return False
    free = BIN_SIZE
    for o in bin:
        free -= o
        if free < obj:
            return False
    return True

def free_size(bin):
    free = BIN_SIZE
    for o in bin:
        free -= o
    return free

objs = [random.randint(20, 101) for _ in range(10)]
print(objs)

#First Fit
bins = []

for obj in objs:
    for b in bins:
        free = BIN_SIZE
        for o in b:
            free -= o
            if free < 0: break
        if free >= obj:
            bin = b
            break
    else:
        bin = []
        bins.append(bin)
    bin.append(obj)
print(bins)

#Next Fit
bins = []
last_bin = None

for obj in objs:
    if not fits(last_bin, obj):
        bin = []
        bins.append(bin)
    bin.append(obj)
    last_bin = bin

print(bins)
#Best Fit
bins = []

for obj in objs:
    fit_bins = list(filter(lambda bin: fits(bin, obj), bins))
    if len(fit_bins) == 0:
        bin = []
        bins.append(bin)
    else:
        bin = min(fit_bins, key = free_size)
    bin.append(obj)
print(bins)

#Worst Fit
bins = []

for obj in objs:
    bin = max(bins, key=free_size) if len(bins) > 0 else None
    if not bin or not fits(bin, obj):
        bin = []
        bins.append(bin)
    bin.append(obj)
print(bins)