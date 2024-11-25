para1="Admittedly, some people may be concerned about national identity diminishing due to increased interaction between countries. Firstly, multinational companies make it difficult for local small or medium corporations to survive. Global corporations produce a large amount of products in factories that can keep merchandise price competitive. Thus, even though similar products made by local companies have higher quality, it's still hard for them to compete on price. This situation would make local corporations lose confidence in their country. Secondly, in certain conservational areas, over-commercialization causes minority cultures to gradually disappear. Moreover, young people excessively admiring foreign cultures makes it harder to preserve traditional cultures."
para2="Admittedly, some people may concern about national identity that would be diminished due to increase interaction within diverse countries. Firstly, multinational companies make it difficult for local small or medium corporations to survive. Because they produce a large amount of product in factory that can keep merchandise price competitive. Even though similar products made by local companies have higher quality, it's still hard to compete on price. This situation would make local corporations loss of confidence and identity with their country. Secondly, for some conservational area, over commercialization cause minority culture gradually disappear. Moreover, young people excessive admire of foreign cultures that make it harder to preserve traditional cultures."

def compare(para1:str,para2:str)->str:
    splited_para1=para1.split(" ")
    splited_para2=para2.split(" ")
    dict_of_para1={}
    for i in range(len(splited_para1)):
        if splited_para1[i] in dict_of_para1:
            dict_of_para1[splited_para1[i]].append(i)
        else:
            dict_of_para1[splited_para1[i]]=[i]


    dict_of_para2={}
    for i in range(len(splited_para2)):
        if splited_para2[i] in dict_of_para2:
            dict_of_para2[splited_para2[i]].append(i)
        else:
            dict_of_para2[splited_para2[i]]=[i]

    p1,p2=0,0

    while p1<len(splited_para1) and p2<len(splited_para2):
        # 正確
        if splited_para1[p1]==splited_para2[p2]:
            p1+=1
            p2+=1
            continue
        # 多字
        if splited_para1[p1] in dict_of_para2:
            flag=False
            for i in range(5):
                # 現在是用神奇數字 之後應該要使用binary search找到離他最近的位置才好
                if p2+i in dict_of_para2[splited_para1[p1]]:
                    for w in splited_para2[p2:p2+i]:
                        print(f"del {w} in para2")
                    p2+=i
                    flag=True
            if flag:
                continue
        # 缺字
        if splited_para2[p2] in dict_of_para1:
            flag=False
            for i in range(5):
                if p1+i in dict_of_para1[splited_para2[p2]]:
                    for w in splited_para1[p1:p1+i]:
                        print(f"add {w} to para2")
                    p1+=i
                    flag=True
            if flag:
                continue
        # 其餘都當作錯字
        print(f"del {splited_para2[p2]} in para2")
        print(f"add {splited_para1[p1]} to para2")
        p1+=1
        p2+=1
    if p1==len(splited_para1):
        print(f"del {splited_para2[p2:]} in para2")
    if p2== len(splited_para2):
        print(f"add {splited_para1[p1:]} to para2")

        


compare(para1,para2)