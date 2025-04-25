BEGIN{
    FS = ","
    OFS = ","
}
{
    print $0
    sum+=$4
    industry[$3]+=$4
}
END{
    asorti(industry,sindustry)
    print"====="
    print "Net : " sum;
    for(i in sindustry){
        key=sindustry[i]
        if(key!="High_industry"){
            print key " : " industry[key];
        }
    }
}