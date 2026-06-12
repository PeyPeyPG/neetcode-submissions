class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_addresses = set()
        for email in emails:
            local,domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            unique_addresses.add(local+domain)
        return len(unique_addresses)