#attempt1:
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=set()
        for i in emails:
            first,second=i.split("@")
            first=first.replace(".","")
            if "+" in first:
                first=first[:first.index("+")]
            s.add(first+"@"+second)
        return len(s)
