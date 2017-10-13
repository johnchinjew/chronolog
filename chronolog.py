import os
import threading

def main():
    entries = {}
    curr_key = ''

    def update_entries():
        if entries.get(curr_key, None) != None:
            entries[curr_key] += 1

    interval(update_entries, 1)

    while (1):
        os.system('cls' if os.name == 'nt' else 'clear')
        for k, v in sorted(entries.items(), key=lambda x:x[1], reverse=1):
            print('* ' if k == curr_key else '  ', end='')
            print('{:<32}'.format(k), format_seconds(v))
        u = input('> ').strip()
        if u == 'q':
            break
        if u == '':
            continue
        if u == '-':
            entries = {}
            continue
        if u[0] == '-':
            entries.pop(u[1:], 0)
            continue
        if not entries.get(u, None):
            entries.update({u: 0})
        curr_key = u


def interval(fn, sec):
    def fn_():
        interval(fn, sec)
        fn()
    t = threading.Timer(sec, fn_)
    t.start()
    return t

def format_seconds(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    f = lambda n: str(n).zfill(2)
    d = '.'
    return f(h) + d + f(m) + d + f(s)

main()
