def arrange_rules(line):
    index, content = line.split(': ')
    if '|' in content:
        rule = [[int(n) for n in rule.split(' ')]
                for rule in content.split(' | ')]
    elif '"' in content:
        rule = content[1:-1]
    else:
        rule = [int(n) for n in content.split(' ')]
    return int(index), rule

def message_check(message, rules):
    current = [(message, rules[0])]
    while current:
        msg, rule = current.pop()
        if not msg and not rule:
            return True
        if not msg or not rule:
            continue
        if isinstance(rule[0], str) and rule[0] == msg[0]:
            current.append((msg[1:], rule[1:]))
        if isinstance(rule[0], int):
            replace = rules[rule[0]]
            if isinstance(replace[0], list):
                for i in replace:
                    current.append((msg, [*i, *rule[1:]]))
            elif isinstance(replace[0], str):
                current.append((msg, [replace, *rule[1:]]))
            else:
                current.append((msg, [*replace, *rule[1:]]))
    return False

def main():
    with open('day19input.txt') as f:
        rules, messages = f.read().split('\n\n')
    messages = messages.splitlines()
    rules = dict(map(arrange_rules, rules.splitlines()))
    print(f'--PART 1-- The answer is: {sum(message_check(msg, rules) for msg in messages)}')

    with open('D:\ztmDevelop\AdventOfCode_2020\day19input.txt') as f:
        rules, messages = f.read().split('\n\n')
    rules = rules.replace('8: 42', '8: 42 | 42 8')
    rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
    messages = messages.splitlines()
    rules = dict(map(arrange_rules, rules.splitlines()))
    print(f'--PART 2-- The answer is: {sum(message_check(msg, rules) for msg in messages)}')
    input()
    
if __name__ == "__main__":
    main()