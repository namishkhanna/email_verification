from django.shortcuts import render
import dns.resolver

# Create your views here.
def main(request):
    if request.method =="GET":
        return render(request,'main.html')

    elif request.method =="POST":

        email = request.POST.get("email")
        domain = email.split('@')[1]
        spam_txt = ['"v=spf1 -all"','"v=spf1 mx -all"',
        '"v=spf1 +a +mx +ip4:198.23.230.251 ~all"','"v=spf1 a mx ip4:173.230.139.246 ~all"',
        '"v=spf1 a mx ~all"','"google-site-verification=-zoE_KGoGJQ_XjTS8q1Q2NtCc3Jf4VLs0PFWryzdjWg"',
        '"google-site-verification=n4eYs3BkKxQ1GuWCGGVg71keNES2ej-2CD8J__Ccfiw"',
        '"v=spf1 mx a ip4:168.119.142.36 ip4:2a01:4f8:251:657:0:0:0:2 -all"',
        '"v=spf1 mx a ip4:168.119.142.36 ip6:2a01:4f8:251:657:0:0:0:2  -all"',
        '"brave-ledger-verification=6234ef29767977faf4b6b02f3b60ffa08ae8299e7f64f584b13b88aae92feed0"']
        count = 0

        try:
            answer = dns.resolver.resolve(domain, "AAAA")[0]
            answer = dns.resolver.resolve(domain, "TXT")[0]
            
            for spam in spam_txt:
                if(spam == f'{answer}'):
                    count = 1

        except:
            count = 1
            
        if(count==1):
            answer = "Spam Email !!!"
        else:
            answer = "Genuine Email ^_^ "

        output = str(email) + " :- " + answer

        return(render(request,'main.html',{'answer' : answer, 'output':output}))