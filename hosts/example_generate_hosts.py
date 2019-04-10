"""
Hosts Generation

Input: my[001..900].domain.com

Output: my001.domain.com, my002.domain.com, ... my900.domain.com
"""

def hosts_generate(inventory):
    """
    Function that will generates a list of hosts based
    in the specific string 'my[001..900].domain.com'
    
    :param inventory: specific string

    returns a list with hosts names.  
    """
    prefix = inventory.split('[')[0]
    first = inventory.replace('..', '[', 1).split('[')[1]
    last = inventory.replace('..', ']', 1).split(']')[1]
    domain = inventory.replace('.', ' ', 3).split(' ')[-1]

    hosts = []

    for x in range(int(first), int(last) + 1):
        
        if len(str(x)) == 1:
            hosts.append('{0}00{1}.{2}'.format(prefix, x, domain))
        elif len(str(x)) == 2:
            hosts.append('{0}0{1}.{2}'.format(prefix, x, domain))
        else:
            hosts.append('{0}{1}.{2}'.format(prefix, x, domain))

    return hosts


if __name__ == "__main__":
    print(hosts_generate(inventory='my[001..900].domain.com'))
