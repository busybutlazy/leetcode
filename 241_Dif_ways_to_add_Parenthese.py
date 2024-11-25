from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        comparison={
            "*":lambda x,y: int(x)*int(y),
            "+":lambda x,y: int(x)+int(y),
            "-":lambda x,y: int(x)-int(y)
        }

        def str2list(expression:str):
            exp_list=[]
            tmp_str=""
            for i in range(len(expression)):
                if expression[i] in comparison:
                    exp_list.append(tmp_str)
                    tmp_str=""
                    exp_list.append(expression[i])
                else:
                    tmp_str+=expression[i]
            exp_list.append(tmp_str)
            return exp_list

        def helper(exp_list,loc)->List[str]:
            return exp_list[:loc-1]+[comparison[exp_list[loc]](exp_list[loc-1],exp_list[loc+1])]+exp_list[loc+2:]

        def compute(exp_list: List) -> List[int]:
            if len(exp_list) == 1: 
                return [int(exp_list[0])]

            results = []
            for i in range(1, len(exp_list), 2):  # Only look at operators
                left_part = compute(exp_list[:i])  # Evaluate left side
                right_part = compute(exp_list[i+1:])  # Evaluate right side
                operator = exp_list[i]

                # Combine results from left and right with the operator
                for left in left_part:
                    for right in right_part:
                        results.append(comparison[operator](left, right))

            return results


        exp_lists=str2list(expression)

        return compute(exp_lists)
        # while len(exp_lists[0])>1:
        #     decode=[]
        #     for i in range(len(exp_lists)):
        #         for j in range(len(exp_lists[i])):
        #             if exp_lists[i][j]=="*":
        #                 decode.append(helper(exp_lists[i],j))
        #             if exp_lists[i][j]=="+":
        #                 decode.append(helper(exp_lists[i],j))
        #             if exp_lists[i][j]=="-":
        #                 decode.append(helper(exp_lists[i],j))
        #     exp_lists=decode

        # for i in range(len(exp_lists)):
        #     exp_lists[i]=exp_lists[i][0]
        
        



        # return exp_lists


        def useless():
            # def permutation(li:List)->List[List]:
            #     if len(li)<2:
            #         return [li]
            #     elif len(li)==2:
            #         return [li,[li[1],li[0]]]
            #     elif len(li)>2:
            #         result=[]
            #         for i in range(len(li)):
            #             tmp=permutation(li[:i]+li[i+1:])
            #             for j in range(len(tmp)):
            #                 result.append([li[i]]+tmp[j])
            #         return result
            
            # calculate_order=permutation(comparison_loc)
            
            # def do_math(order:List,expression:str)->int:
            #     compare=order.pop()
            #     tmp_ans=str(comparison[expression[compare]](expression[compare-1],expression[compare+1]))
            #     if order == 0:
            #         return tmp_ans
            #     else:
            #         return do_math(order,expression[:compare-1]+expression[compare+2:])
            pass


                




if __name__=="__main__":
    sol=Solution()
    expression = "0"
    print(sol.diffWaysToCompute(expression))