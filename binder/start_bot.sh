ADDR='bot@example.com'
PASSWORD='myPassword'

simplebot --basedir ~/bots/`echo $ADDR|tr "@" "_"` init $ADDR "$PASSWORD"
simplebot --basedir ~/bots/`echo $ADDR|tr "@" "_"` serve
