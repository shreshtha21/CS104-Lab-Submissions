BEGIN{
    FS =","
    OFS=","
}
NR==1{
    print $0, "Email-ID"
    next
}
{
    email = $2 $4"@surveycorps.com"
    print$0,email
}
