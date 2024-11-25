from typing import List

class Sparse_Matrix():
    def __init__(self) -> None:
        """
        This only can use in matrix.
        Zip function can decrease the data.
        """
        pass
    
    
    def mat_zip(mat:List[List],most_num:int=0)->List[int]:
        shape=[]
        tmp=mat
        while type(tmp)==list and len(tmp)>0:
            shape.append(len(tmp))
            tmp=tmp[0]
        zip_list=[]
        zip_list.append(shape+[most_num])
        def __recursive(sub_mat:List[List],location:List[int])->None:
            if type(sub_mat)==list and len(sub_mat)>0 and type(sub_mat[0])==list:
                for i in range(len(sub_mat)):
                    __recursive(sub_mat[i],location+[i])
            elif type(sub_mat)==list and len(sub_mat)>0 and type(sub_mat[0])==int:
                for i in range(len(sub_mat)):
                    if sub_mat[i]!=0:
                        zip_list.append(location+[i]+[sub_mat[i]])
        __recursive(mat,[])
        return zip_list
    
    def mat_unzip(zip_list:List[int])->List[List]:
        shape=zip_list[0][:-1]
        
        def __recursive_mat_maker(shape,val):
            if len(shape)==1:
                return [val]*shape[0]
            else:
                mat=[]
                for i in range(shape[0]):
                    mat.append(__recursive_mat_maker(shape[1:],val))
                return mat

        mat=__recursive_mat_maker(shape,zip_list[0][-1])
        def __recursive_writer(data:List[int],sub_mat:List[List])->None:
            if len(data)==2:
                sub_mat[data[0]]=data[1]
            else:
                __recursive_writer(data[1:],sub_mat[data[0]])
        
        for data in zip_list[1:]:
            __recursive_writer(data,mat)
        return mat

    def transpose():
        """
        2D matrix only.
        """
        
        
        pass

if __name__=="__main__":
    mat=[
        [[25,0,0,0,0,0,0,0],[32,0,0,0,0,0,0,-25]],
        [[0,33,0,0,0,0,0,77],[0,0,0,0,0,0,0,0]],
        [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
        [[101,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
        [[0,0,38,0,0,0,0,0],[0,0,1,0,0,0,0,0]]
         ]
    
    zip_list=Sparse_Matrix.mat_zip(mat)
    print(zip_list)
    print(Sparse_Matrix.mat_unzip(zip_list))