ContactPageMap = dict(FirstNameFieldXpath  = "//input[contains(@name, 'first')]",
                      LastNameFieldXpath   = "//input[contains(@name, 'last')]",
                      EmailFieldXpath      = "(//input[contains(@id, 'input')])[3]",
                      CommentFieldXpath    = "//textarea",
                      SubmitButtonXpath    = "//span[.='Submit']",
                      ThankYouMessageXpath = "//div[contains(text(), 'Thank you')]"
)


ProductPageMap = dict(QuantityDropDownID     = "wsite-com-product-option-Quantity",
                      TwitterShareLinkXpath = "//a[@title='Share on Twitter']"
)

TwitterLoginPageMap = dict(UsernameFieldID         = "username_or_email",
                           PasswordFieldID         = "password",
                           SignAndTweetButtonXpath = "//input[@type = 'submit']"
)

ShareOnTwitterPageMap = dict(TweetButtonxpath = "//input[@value = 'Tweetar']",
							 CommentFieldId  = "status"
)
