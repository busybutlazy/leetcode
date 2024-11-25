from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queues=deque()
        curr=root
        l,r=float("-inf"),float("inf")
        while curr:
            print("curr.val=",curr.val,"l=",l,"r=",r)
            
            if curr.val<=l or curr.val>=r:
                return False
            
            if curr.left:
                queues.append((curr.left,l,curr.val))
            if curr.right:
                queues.append((curr.right,curr.val,r))
            if queues:
                curr,l,r=queues.popleft()
            else:
                curr=None
        return True


def tree_maker(li_of_node):
    l=len(li_of_node)
    for i in range(l):
        if not li_of_node[i]:
            continue
        li_of_node[i]=TreeNode(li_of_node[i])

    for i in range(l):
        if not li_of_node[i]:
            continue
        left=i*2+1
        right=i*2+2
        if left < len(li_of_node):
            li_of_node[i].left=li_of_node[left]
        if right < len(li_of_node):
            li_of_node[i].right=li_of_node[right]
    return li_of_node[0]



def tree_printer(head):
    if not head:
        return
    print(head.val)
    tree_printer(head.left)
    tree_printer(head.right)

if __name__=="__main__":
    solution=Solution()
    li=[120,70,140,50,100,130,160,20,55,75,110,119,
        135,150,200]
    # li=[3,None,30,10,None,None,15,None,45]
    # li=[2147483647]
    # li=[9963,9923,9996,9900,None,None,None,9895,None,9894,None,9879,None,9852,None,9845,None,9843,None,9784,None,9772,None,9767,None,9766,None,9757,None,9723,None,9714,None,9670,None,9663,None,9646,None,9590,None,9590,None,9578,None,9544,None,9482,None,9479,None,9414,None,9412,None,9411,None,9389,None,9364,None,9351,None,9351,None,9344,None,9332,None,9331,None,9272,None,9253,None,9226,None,9192,None,9185,None,9146,None,9124,None,9064,None,9061,None,8987,None,8963,None,8911,None,8905,None,8903,None,8879,None,8847,None,8834,None,8834,None,8825,None,8819,None,8798,None,8787,None,8772,None,8763,None,8761,None,8759,None,8716,None,8706,None,8705,None,8700,None,8681,None,8648,None,8633,None,8605,None,8599,None,8594,None,8585,None,8558,None,8533,None,8491,None,8480,None,8424,None,8419,None,8418,None,8408,None,8371,None,8366,None,8341,None,8316,None,8303,None,8238,None,8200,None,8198,None,8183,None,8178,None,8176,None,8113,None,8092,None,8064,None,8029,None,8022,None,7977,None,7957,None,7952,None,7931,None,7923,None,7912,None,7877,None,7832,None,7830,None,7785,None,7730,None,7726,None,7717,None,7699,None,7686,None,7672,None,7633,None,7625,None,7608,None,7597,None,7575,None,7548,None,7547,None,7512,None,7499,None,7482,None,7403,None,7388,None,7366,None,7324,None,7324,None,7321,None,7306,None,7301,None,7299,None,7295,None,7210,None,7167,None,7134,None,7127,None,7117,None,7075,None,7060,None,6999,None,6993,None,6988,None,6941,None,6918,None,6890,None,6883,None,6830,None,6812,None,6764,None,6757,None,6749,None,6747,None,6732,None,6686,None,6657,None,6636,None,6610,None,6607,None,6606,None,6575,None,6573,None,6565,None,6518,None,6510,None,6463,None,6445,None,6425,None,6410,None,6402,None,6392,None,6370,None,6368,None,6346,None,6334,None,6315,None,6285,None,6284,None,6240,None,6223,None,6197,None,6160,None,6158,None,6148,None,6131,None,6060,None,6032,None,6003,None,5956,None,5937,None,5919,None,5913,None,5904,None,5894,None,5869,None,5854,None,5854,None,5817,None,5806,None,5794,None,5794,None,5770,None,5728,None,5722,None,5717,None,5688,None,5673,None,5663,None,5649,None,5639,None,5605,None,5604,None,5594,None,5573,None,5561,None,5545,None,5540,None,5536,None,5530,None,5529,None,5516,None,5507,None,5471,None,5435,None,5377,None,5365,None,5356,None,5317,None,5291,None,5238,None,5175,None,5153,None,5112,None,5111,None,5091,None,5085,None,5080,None,5079,None,5045,None,5041,None,5039,None,5034,None,5000,None,4983,None,4941,None,4925,None,4911,None,4899,None,4890,None,4884,None,4879,None,4874,None,4862,None,4859,None,4829,None,4821,None,4803,None,4801,None,4782,None,4765,None,4760,None,4756,None,4738,None,4716,None,4687,None,4678,None,4675,None,4627,None,4556,None,4553,None,4485,None,4431,None,4420,None,4412,None,4398,None,4394,None,4347,None,4344,None,4336,None,4286,None,4246,None,4245,None,4187,None,4172,None,4167,None,4145,None,4124,None,4098,None,4081,None,4080,None,4073,None,4006,None,3928,None,3914,None,3913,None,3907,None,3903,None,3893,None,3892,None,3891,None,3860,None,3844,None,3841,None,3794,None,3790,None,3769,None,3760,None,3751,None,3750,None,3746,None,3723,None,3723,None,3718,None,3713,None,3713,None,3710,None,3682,None,3679,None,3665,None,3644,None,3639,None,3636,None,3632,None,3621,None,3615,None,3554,None,3538,None,3505,None,3490,None,3466,None,3408,None,3395,None,3392,None,3340,None,3321,None,3301,None,3262,None,3195,None,3187,None,3172,None,3165,None,3104,None,3103,None,2955,None,2933,None,2927,None,2888,None,2881,None,2851,None,2845,None,2839,None,2835,None,2827,None,2803,None,2798,None,2776,None,2736,None,2733,None,2709,None,2702,None,2698,None,2684,None,2669,None,2661,None,2633,None,2632,None,2628,None,2627,None,2617,None,2609,None,2606,None,2587,None,2558,None,2516,None,2485,None,2463,None,2437,None,2367,None,2365,None,2351,None,2312,None,2289,None,2286,None,2286,None,2273,None,2255,None,2252,None,2208,None,2205,None,2194,None,2190,None,2089,None,2075,None,2056,None,2037,None,2031,None,2021,None,2017,None,1952,None,1857,None,1849,None,1826,None,1806,None,1802,None,1797,None,1792,None,1770,None,1760,None,1755,None,1734,None,1734,None,1716,None,1701,None,1675,None,1668,None,1667,None,1659,None,1652,None,1633,None,1630,None,1604,None,1596,None,1595,None,1575,None,1573,None,1562,None,1556,None,1548,None,1535,None,1533,None,1507,None,1506,None,1499,None,1467,None,1440,None,1407,None,1396,None,1353,None,1343,None,1342,None,1318,None,1304,None,1253,None,1182,None,1165,None,1153,None,1118,None,1076,None,1045,None,1012,None,961,None,955,None,950,None,937,None,936,None,923,None,883,None,849,None,839,None,838,None,823,None,820,None,815,None,801,None,800,None,791,None,758,None,738,None,734,None,718,None,712,None,709,None,656,None,649,None,627,None,611,None,610,None,609,None,602,None,597,None,548,None,514,None,507,None,487,None,441,None,401,None,375,None,372,None,367,None,337,None,327,None,316,None,306,None,298,None,265,None,219,None,217,None,198,None,191,None,188,None,163,None,87,None,84,None,40,None,-5,None,-17,None,-39,None,-69,None,-72,None,-143,None,-145,None,-169,None,-180,None,-206,None,-213,None,-213,None,-244,None,-245,None,-254,None,-302,None,-303,None,-317,None,-319,None,-343,None,-349,None,-375,None,-398,None,-416,None,-417,None,-417,None,-448,None,-495,None,-567,None,-580,None,-588,None,-590,None,-593,None,-618,None,-624,None,-668,None,-730,None,-736,None,-750,None,-756,None,-765,None,-766,None,-809,None,-817,None,-834,None,-843,None,-858,None,-871,None,-921,None,-921,None,-923,None,-932,None,-936,None,-954,None,-991,None,-991,None,-1010,None,-1065,None,-1117,None,-1166,None,-1203,None,-1232,None,-1261,None,-1268,None,-1330,None,-1331,None,-1332,None,-1362,None,-1379,None,-1434,None,-1473,None,-1501,None,-1502,None,-1503,None,-1523,None,-1538,None,-1546,None,-1640,None,-1641,None,-1656,None,-1686,None,-1688,None,-1721,None,-1741,None,-1790,None,-1817,None,-1831,None,-1843,None,-1846,None,-1862,None,-1863,None,-1881,None,-1887,None,-1913,None,-1915,None,-1932,None,-1939,None,-1941,None,-1984,None,-1984,None,-2002,None,-2013,None,-2073,None,-2083,None,-2089,None,-2102,None,-2103,None,-2155,None,-2168,None,-2173,None,-2176,None,-2182,None,-2198,None,-2239,None,-2251,None,-2266,None,-2301,None,-2323,None,-2380,None,-2405,None,-2414,None,-2427,None,-2433,None,-2448,None,-2459,None,-2466,None,-2467,None,-2477,None,-2483,None,-2489,None,-2492,None,-2540,None,-2554,None,-2582,None,-2596,None,-2597,None,-2601,None,-2603,None,-2651,None,-2652,None,-2671,None,-2681,None,-2685,None,-2689,None,-2693,None,-2701,None,-2710,None,-2755,None,-2755,None,-2765,None,-2775,None,-2791,None,-2822,None,-2826,None,-2836,None,-2842,None,-2862,None,-2880,None,-2942,None,-2970,None,-2986,None,-3016,None,-3023,None,-3040,None,-3064,None,-3075,None,-3087,None,-3123,None,-3160,None,-3179,None,-3215,None,-3215,None,-3224,None,-3230,None,-3241,None,-3279,None,-3286,None,-3288,None,-3289,None,-3307,None,-3343,None,-3361,None,-3367,None,-3387,None,-3395,None,-3409,None,-3427,None,-3431,None,-3447,None,-3464,None,-3508,None,-3541,None,-3566,None,-3581,None,-3659,None,-3711,None,-3720,None,-3730,None,-3735,None,-3752,None,-3760,None,-3760,None,-3776,None,-3793,None,-3825,None,-3851,None,-3854,None,-3860,None,-3874,None,-3897,None,-3960,None,-3968,None,-4032,None,-4034,None,-4048,None,-4077,None,-4122,None,-4141,None,-4154,None,-4186,None,-4372,None,-4411,None,-4511,None,-4516,None,-4530,None,-4545,None,-4548,None,-4548,None,-4554,None,-4580,None,-4582,None,-4596,None,-4613,None,-4622,None,-4665,None,-4668,None,-4669,None,-4669,None,-4678,None,-4682,None,-4726,None,-4769,None,-4778,None,-4794,None,-4797,None,-4800,None,-4812,None,-4829,None,-4838,None,-4874,None,-4895,None,-4905,None,-4907,None,-4958,None,-4971,None,-5007,None,-5025,None,-5033,None,-5057,None,-5062,None,-5063,None,-5065,None,-5072,None,-5086,None,-5101,None,-5144,None,-5149,None,-5170,None,-5179,None,-5188,None,-5193,None,-5194,None,-5201,None,-5247,None,-5269,None,-5295,None,-5338,None,-5373,None,-5380,None,-5400,None,-5401,None,-5410,None,-5413,None,-5426,None,-5427,None,-5546,None,-5549,None,-5581,None,-5622,None,-5633,None,-5645,None,-5664,None,-5664,None,-5666,None,-5672,None,-5674,None,-5675,None,-5678,None,-5720,None,-5722,None,-5785,None,-5799,None,-5804,None,-5821,None,-5823,None,-5823,None,-5867,None,-5872,None,-5891,None,-5891,None,-5892,None,-5892,None,-5923,None,-5939,None,-5949,None,-5954,None,-5956,None,-5982,None,-5999,None,-6008,None,-6027,None,-6049,None,-6053,None,-6061,None,-6069,None,-6078,None,-6092,None,-6099,None,-6145,None,-6166,None,-6186,None,-6231,None,-6252,None,-6254,None,-6328,None,-6382,None,-6396,None,-6401,None,-6406,None,-6410,None,-6417,None,-6427,None,-6428,None,-6449,None,-6465,None,-6481,None,-6487,None,-6512,None,-6522,None,-6523,None,-6543,None,-6582,None,-6591,None,-6625,None,-6629,None,-6663,None,-6678,None,-6687,None,-6740,None,-6743,None,-6761,None,-6774,None,-6788,None,-6809,None,-6818,None,-6833,None,-6866,None,-6878,None,-6892,None,-6940,None,-6959,None,-6977,None,-7066,None,-7126,None,-7153,None,-7155,None,-7188,None,-7230,None,-7248,None,-7268,None,-7323,None,-7336,None,-7395,None,-7396,None,-7397,None,-7425,None,-7444,None,-7488,None,-7494,None,-7522,None,-7551,None,-7591,None,-7602,None,-7603,None,-7611,None,-7659,None,-7692,None,-7697,None,-7768,None,-7776,None,-7780,None,-7805,None,-7828,None,-7836,None,-7867,None,-7910,None,-7928,None,-7934,None,-7936,None,-7955,None,-7960,None,-7989,None,-8007,None,-8087,None,-8093,None,-8103,None,-8104,None,-8115,None,-8223,None,-8229,None,-8230,None,-8279,None,-8286,None,-8326,None,-8365,None,-8397,None,-8511,None,-8530,None,-8552,None,-8555,None,-8659,None,-8679,None,-8687,None,-8737,None,-8748,None,-8754,None,-8763,None,-8763,None,-8785,None,-8807,None,-8815,None,-8891,None,-8898,None,-8901,None,-8903,None,-8915,None,-8920,None,-8967,None,-8976,None,-9002,None,-9007,None,-9037,None,-9039,None,-9042,None,-9066,None,-9137,None,-9153,None,-9159,None,-9161,None,-9186,None,-9193,None,-9204,None,-9234,None,-9343,None,-9343,None,-9362,None,-9364,None,-9408,None,-9411,None,-9434,None,-9436,None,-9488,None,-9506,None,-9517,None,-9518,None,-9594,None,-9643,None,-9646,None,-9655,None,-9684,None,-9745,None,-9769,None,-9769,None,-9792,None,-9815,None,-9816,None,-9823,None,-9828,None,-9833,None,-9833,None,-9849,None,-9879,None,-9885,None,-9912,None,-9914,None,-9927]
    print(solution.isValidBST(tree_maker(li)))

        