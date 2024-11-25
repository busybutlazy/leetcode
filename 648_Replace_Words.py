from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        # Creat a dictionary which key=char , value=(dictionary of next char) or (the root). 
        dict_by_char={}
        def make_dict_by_char(root:str,d:dict,replace_root:str):
            # If all the char in root are in dictionary. We can put the "full-root" in dictionary.
            if len(root)==1:
                d.update({root[0]:replace_root})
            
            if root[0] in d:
                # It means there is a root shorter than this root. 
                # Because this quest should replace word with shortest root. 
                # So can skip the longer one.
                if type(d[root[0]])==str:
                    return
            else:
                new_d={}
                d.update({root[0]:new_d})
            # Recursive if there's char of root not become dictionary.
            make_dict_by_char(root[1:],d[root[0]],replace_root)

        # Put every root in the function we made to make the dictionary "dict_by_char".
        for root in dictionary:
            make_dict_by_char(root,dict_by_char,root)
        
        

        # Split the sentence by " ".
        sentence_words=sentence.split(" ")
        
        print("sentence_words=",sentence_words)

        # A function put each word inside.
        def check_root_by_char(word:str,d:dict):
            # If the word is shorter than root. 
            # It means this word don't have the root in the dictionary.
            if len(word)==0:
                return False
            
            # If the first char is in dictionary.
            if word[0] in d:
                # If the dictionary contain the "full-root". Then return the "full-root".
                if type(d[word[0]])==str:
                    return d[word[0]]
                else:
                    # Otherwise keep checking the next char.
                    return check_root_by_char(word[1:],d[word[0]])
            
            # If the first char is not in dictionary.
            # It means this word don't have the root in the dictionary.
            return False
        
        result=""

        for word in sentence_words:
            # temp contain "full-root"(there is a root can replace with) or False.
            temp=check_root_by_char(word,dict_by_char)
            if temp:
                result+=temp+" "
            else:
                result+=word+" "
        
        # don't return the trailing spaces.
        return result[:-1]
    
if __name__=="__main__":
    solution=Solution()
    dictionary = ["cat","bat","rat","carry"]
    # dictionary=["e","k","c","harqp","h","gsafc","vn","lqp","soy","mr","x","iitgm","sb","oo","spj","gwmly","iu","z","f","ha","vds","v","vpx","fir","t","xo","apifm","tlznm","kkv","nxyud","j","qp","omn","zoxp","mutu","i","nxth","dwuer","sadl","pv","w","mding","mubem","xsmwc","vl","farov","twfmq","ljhmr","q","bbzs","kd","kwc","a","buq","sm","yi","nypa","xwz","si","amqx","iy","eb","qvgt","twy","rf","dc","utt","mxjfu","hm","trz","lzh","lref","qbx","fmemr","gil","go","qggh","uud","trnhf","gels","dfdq","qzkx","qxw"]
    sentence = "the cattle was rattled by the battery"
    # sentence="ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww vhokchxz dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna ipfzhuvgo daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp"
    print(solution.replaceWords(dictionary,sentence))