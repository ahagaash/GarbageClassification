# From pdf_mail Library
from pdf_mail import sendpdf

def sendEmailToUser(wastetype,userid,filename):
    if wastetype == "metal":
        k = sendpdf("agroup482@gmail.com",
                    userid,
                    "aophtzjowhwxbojd",
                    "Waste collectors information",
                    "Waste is detected as " +wastetype,
                    filename,
                    "./pdf/")
        k.email_send()

    if wastetype == "glass":
        k = sendpdf("agroup482@gmail.com",
                    userid,
                    "aophtzjowhwxbojd",
                    "Waste collectors information",
                    "Waste is detected as "+wastetype,
                    filename,
                    "./pdf/")
        k.email_send()

    if wastetype == "plastic":
        k = sendpdf("agroup482@gmail.com",
                    userid,
                    "aophtzjowhwxbojd",
                    "Waste collectors information",
                    "Waste is detected as "+wastetype,
                    filename,
                    "./pdf/")
        k.email_send()





#sendEmailToUser("plastic","ahagaash@gmail.com")



def sendEmailToUserbasedonAddress(wastetype,userid,filename):
    if wastetype == "metal":
        k = sendpdf("agroup482@gmail.com",
                    userid,
                    "aophtzjowhwxbojd",
                    "Waste collectors information",
                    "Waste is detected as " +wastetype,
                    filename,
                    "./pdf/")
        k.email_send()

    if wastetype == "glass":
        k = sendpdf("agroup482@gmail.com",
                    userid,
                    "aophtzjowhwxbojd",
                    "Waste collectors information based on your Address",
                    "Waste is detected as "+wastetype,
                    filename,
                    "./pdf/")
        k.email_send()

    if wastetype == "plastic":
        k = sendpdf("agroup482@gmail.com",
                    userid,
                    "aophtzjowhwxbojd",
                    "Waste collectors information",
                    "Waste is detected as "+wastetype,
                    filename,
                    "./pdf/")
        k.email_send()










# Create an object of sendpdf function

#sendEmailToUser("plastic","ahagaash@gmail.com")
# sending an email
