import dns.resolver

email = 'grr.la'

while 1:
    try: 
        answer = dns.resolver.resolve(email, "A")
        print(answer[0])
    except dns.resolver.NoAnswer:
        print("No AAAA")
    except dns.resolver.NXDOMAIN:
        print("No such domain")
    except KeyboardInterrupt:
        print ("\nGoodbye!")
        exit()
        answer = dns.resolver.resolve(email, "A")[0]

        if(answer):
            answer = "Yes"
        elif(answer == "NXDOMAIN"):
            answer = "No"