class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1 :return 10 
        M=int(1e9+7)
        dp_result=[2,2,2,2,3,0,3,2,2,2]
        for _ in range(n-2):
            new_result=[
                (dp_result[4]+dp_result[6])%M,
                (dp_result[6]+dp_result[8])%M,
                (dp_result[7]+dp_result[9])%M,
                (dp_result[4]+dp_result[8])%M,
                (dp_result[0]+dp_result[3]+dp_result[9])%M,
                0,
                (dp_result[0]+dp_result[1]+dp_result[7])%M,
                (dp_result[2]+dp_result[6])%M,
                (dp_result[1]+dp_result[3])%M,
                (dp_result[2]+dp_result[4])%M
            ]
        return sum(dp_result)
