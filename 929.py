class Solution:
    def numUniqueEmails(self, emails):
        mapping = {}
        for email in emails:
            local, ip = email.split('@', 1)
            local_res = ''
            for c in local:
                if c == '+':
                    break
                elif c == '.':
                    continue
                else:
                    local_res += c
            if ip in mapping:
                mapping[ip].append(local_res)
            else:
                mapping[ip] = [local_res]
        res = 0
        for value in mapping.values():
            res += len(set(value))
        return value

    def numUniqueEmails2(self, emails):
        clean_list = []
        for email in emails:
            name, ip = email.split('@', 1)
            if '+' in name:
                name = name[0:name.find('+')]
            name = name.replace('.', '')
            clean_list.append(name + '@' + ip)
        return len(set(clean_list))
