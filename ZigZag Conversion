class Solution(object):
    def convert(self, s, numRows):
        final_result="";
        map=dict();
        n=0;
        if numRows==1:
            final_result=s;
        elif(len(s)>0):
            numRows=min(numRows,len(s));
            for n in range(numRows):
                map[n]=s[n];
            for i in range(numRows,len(s)):
                if n==0:
                    dir=1;
                elif n==numRows-1:
                    dir=-1;
                n=n+dir;
                map[n]=map[n]+s[i];
            for n in range(numRows):
                final_result=final_result+map[n];
            print final_result;
        return final_result
        
