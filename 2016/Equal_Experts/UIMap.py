from Equal_Experts.Constants               import EE_Constants


HomePageMap = dict(   SignUpLinkXpath          = "//a[contains(text(),'Sign up')]",
                      SignInLinkXpath          = "//a[contains(text(),'Sign in')]",
                      RefreshLinkXpath         = "//a[contains(text(),'Refresh')]",
                      HomeLinkXpath            = "//a[.='Home']",
                      CheddarMACLinkXpath      = "(//a[.='Homepage'])[1]",
                      CheddarMACAllSnippetsLinkXpath      = "(//a[.='All snippets'])[1]",
                      BrieLinkXpath      = "(//a[.='Homepage'])[2]",
                      BrieSnippetsLinkXpath      = "(//a[.='All snippets'])[2]"
)

SignUpPageMap = dict( UsernameFieldXpath          = "//input[@name='uid']",
                      PasswordFieldXpath          = "//input[@name='pw']",
                      CreateAccountButtonXpath    = "//input[@value = 'Create account']"
)

SignInPageMap = dict( UsernameFieldXpath          = "//input[@name='uid']",
                      PasswordFieldXpath          = "//input[@name='pw']",
                      LoginButtonXpath            = "//input[@value = 'Login']"
)

AccountCreatedPageMap = dict( MessageFieldXpath   = "//div[contains(text(),'Account created')]"
)

LoggedInPoductPageMap = dict( UserFieldXpath   = "//span[contains(text(),"+EE_Constants['SignUp_Username']+")]",
                              NewSnippetLinkXpath = "//a[contains(text(),'New') and contains(text(),'Snippet')]",
                              UploadLinkXpath = "//a[contains(text(),'Upload')]"
)

NewSnippetPageMap = dict(     SnippetTextBoxXpath = "//textarea[@name='snippet']",
                              SubmitButtonXpath = "//input[@value='Submit']"


)

MySnippetsPageMap = dict(     AllSnippetsBoxXpath = "//div[@class='content']"


)

UploadPageMap = dict(     UploadButtonXpath = "//input[@value='Upload']",
                          UploadFieldXpath = "//input[@name='upload_file']"


)

UploadCompletedPageMap = dict(     UploadCompletedTextXpath = "//h2[contains(text(),'Upload Complete')]"

)