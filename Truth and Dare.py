for i in range(int(input())):
    tr=int(input())
    arr_tr=list(map(int,input().split()))
    dr=int(input())
    arr_dr=list(map(int,input().split()))
    ts=int(input())
    arr_ts=list(map(int,input().split()))
    ds=int(input())
    arr_ds=list(map(int,input().split()))
    arr_tr=set(arr_tr)
    arr_dr=set(arr_dr)
    arr_ds=set(arr_ds)
    arr_ts=set(arr_ts)
    
    if arr_ts.issubset(arr_tr) and arr_ds.issubset(arr_dr):
        print("yes")
    else:
        print("no")
