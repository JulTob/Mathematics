def LoadPrimes(filename='primes.txt'):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            return [int(x) for x in content.split(',') if x.strip()]
    except FileNotFoundError:
        return [2]  # start with the first prime

def SavePrimes(primes, filename='primes.txt'):
    with open(filename, 'w') as file:
        file.write(','.join(str(p) for p in primes))
        
def IsPrime(n,primes):
    if n in primes: return True
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def NextPrimeList(primes):
    # Compute N = product of known primes + 1
    N = 1
    for p in primes:
        N *= p
    N += 1
    i = 2
    # Find the smallest prime factor not in the list
    while i<=N:
      if IsPrime(i,primes):
        if N % i == 0 and i not in primes:
          primes.append(i)
          while N%i == 0:
            N = N//i
          break 
      i += 1
    
    return primes

def SimulateEuclidProof(primes = LoadPrimes(filename='primes.txt') ):
    print(f"Current primes: {primes}")
    primes = NextPrimeList(primes)
    print(f"Final list: {primes}")
    SavePrimes(primes, filename='primes.txt')

SimulateEuclidProof()
