import sys

red = "\033[31m"
end_color = "\033[0m"
required = '+'

hosts = [ 'add-host', 'show-host', 'set-host', 'delete-host', 'show-hosts' ]
network = [ 'add-network', 'show-network', 'set-network', 'delete-network', 'show-networks' ]
group = [ 'add-group', 'show-group', 'set-group', 'delete-group', 'show-groups' ]
policy = [ 'verify-policy', 'install-policy' ]
package = [ 'add-package', 'show-package', 'set-package', 'delete-package', 'show-packages' ]

nat_settings = [ '+auto-rule', '+ip-address | ipv4-address | ipv6-address', 'hide-behind', 'install-on', 'method' ]

params = {
        'add-host'       : [ '+name', '+ip-address | ipv4-address | ipv6-address', 'tags'],
        'show-host'      : [ '+uid | name' ],
        'set-host'       : [ '+uid | name', 'ip-address | ipv4-address | ipv6-address', 'new-name', 'tags', 'color'],
        'delete-host'    : [ '+uid | name' ],
        'show-hosts'     : [],
        'add-network'    : [ '+name', '+subnet | subnet4 | subnet6', '+mask-length | mask-length4 | mask-length6 | subnet-mask', 
            'color', 'comments', 'tags' ],
        'show-network'   : [ '+uid | name' ],
        'set-network'    : [ '+uid | name', 'subnet | subnet4 | subnet6 | mask-length | mask-length4 | subnet-mask', nat_settings,
            'new-name', 'tags' ],
        'delete-network' : [ '+uid | name' ],
        'show-networks'  : [ 'limit', 'offset', 'show-membership' ],
        'add-group'      : [ '+name', 'members', 'tags', 'color', 'comments' ],
        'show-group'     : [ '+uid | name', 'details-level = uid | standard | full (default = standard)'],
        'set-group'      : [ '+uid | name', 'members', 'new-name', 'tags', 'color', 'comments' ],
        'delete-group'   : [ '+uid | name' ],
        'show-groups'    : [ 'limit', 'offset'],
        'verify-policy'  : [ '+policy-package' ],
        'install-policy' : [ '+policy-package', 'access', 'desktop-security', 'install-on-all-cluster-members-or-fail', 'prepare-only', 'qos', 
            'revision', 'targets', 'threat-prevention' ],
        'add-package'    : [ '+name', 'access', 'desktop-security', 'installation-targets', 'qos', 'qos-policy-type', 'tags', 'threat-prevention', 
            'vpn-traditional-mode', 'color', 'comments', 'details-level', 'ignore-warning', 'ignore-errors' ],
        'show-package'   : [ '+uid | name', 'details-level = uid | standard | full (default = standard)' ],
        'set-package'    : [ '+uid | name', 'access', 'access-layers', 'desktop-security', 'installation-targets', 'new-name', 'qos', 'qos-policy-type',
            'tags', 'threat-layers', 'threat-prevention', 'vpn-traditional-mode', 'color', 'comments', 'ignore-warning', 'ignore-errors' ],
        'delete-package' : [ '+uid | name', 'details-level = uid | standard | full (default = standard)', 'ignore-warnings', 'ingore-errors' ],
        'show-packages'  : [ 'limit', 'offset', 'order', 'details-level = uid | standard | full (default = standard)' ]
        }

subjects = {
        'host'  : [ 'host', hosts ],
        'net'   : [ 'network', network ],
        'group' : [ 'group', group ],
        'pol'   : [ 'policy', policy ],
        'pack'  : [ 'package', package ]
        }


def print_params(params):

    for param in params:
        if list is type(param):
            print_params(param)
        elif required in param:
            sys.stdout.write(red + param.replace(required, '') + end_color + '\n\t\t')
        else:
            sys.stdout.write(param + '\n\t\t')

def detect(arg):

    for subject in subjects:
        #print ("Checking %s" % (subject))
        if subject in arg:
        #    print (subject)
        #    print ("Found %s in %s." % (subject, arg))
        #    print ("Going to print out these commands")
        #    print (subjects[subject])
            return subject
    return None

def helper(arg):

    #if 'host' in arg:
    printme = detect(arg)
    if None is not detect(arg):
        print("%s commands: " % (subjects[printme][0]))
        print("[command]\t{parameter(s)}")
        for item in subjects[printme][1]:
            sys.stdout.write(item + '\t')
            print_params(params[item])
            sys.stdout.write('\n')
        print("%sRed is a required parameter%s" % (red, end_color))
    else:
        print ("Couldn't find anything related.")
