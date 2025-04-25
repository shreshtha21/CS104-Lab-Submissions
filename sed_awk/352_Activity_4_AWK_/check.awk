BEGIN{
    for(i=0;i<=TOTAL-1;i++){
        noproduced[i]=0;
        noconsumed[i]=0;
    }
    for(i=0;i<=NUM_MAS-1;i++){
        maspresent[i]=0;
        masexit[i]=0;
    }
    for(i=0;i<=NUM_WOR-1;i++){
        worpresent[i]=0;
        worexit[i]=0;
    }
    result="YES"
}
{
    if($1=="Produced"){
        if(maspresent[$5]==0 && $5<NUM_MAS){
             count = 0;
            for (name in buffer) {
            count++;
            }
            if(count<BUF_SIZE){
            buffer[$2]=1
            noproduced[$2]++
            }else {
            result="NO"
        }
        }else result="NO"
    }else if($1=="Consumed" && noproduced[i]!=0){
            if(worpresent[$5]==0 && $5<NUM_WOR){
            delete buffer[$2]
            noconsumed[$2]++
        }else{
            result="NO"
        }
    }else if($1=="Master"){
        maspresent[$2]=-1
        masexit[$2]++
    }else {
        worpresent[$2]=-1
        worexit[$2]++
    }
    for(i in buffer){
        printf "%s ", i;
    }
    print ""
}
END{
    for(i in noproduced){
        if(noproduced[i]!=1)result="NO"
    }
    for(i in noconsumed){
        if(noconsumed[i]!=1)result="NO"
    }
    for(i in masexit){
        if(masexit[i]!=1 && masexit[i]!=0)result="NO"
    }
    for(i in worexit){
        if(worexit[i]!=1 && masexit[i]!=0)result="NO"
    }
    print result
}