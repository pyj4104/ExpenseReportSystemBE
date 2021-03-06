# Type of inputs
TYPEOFINPUT = 'type'
INTEGER = 'integer'
STRING = 'string'
LIST = 'list'
SCHEMA = 'schema'
DICT = 'dict'

# Properties
ALLOWED = 'allowed' 	# for allowed list
EMPTY = 'empty'			# for empty fields
CASTER = 'coerce'		# casting to other type
REQUIRED = 'required'	# check if required
REGEX = 'regex'			# check uisng regex
TWOPLACES = '.01'		# for quantizing the finance info

# Regexes
REGEXEMAIL = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEXKORNAME = '^[가-힣]{1,4}$'
REGEXLEGALNAME = '^[a-zA-Z,.\'-]+$'
REGEXSECCODE = '^[0-9a-zA-Z]{6}$'
REGEXMONEY = '^[1-9][0-9]{0,9}[\.]?[\d]{0,2}$'
REGEXCATEGORIES = '^[0-9a-zA-Z가-힣 ]+$'
REGEXDATE = '^[0-9]{4}-(0[1-9]|1[0-2]|[1-9])-(0[1-9]|1\d|2\d|3[0-1]|[1-9])$'
REGEXINTEGER = '^\d{1,10}$'

# Accepted Image Extensions
ACCEPTEDEXT = set(['jpg', 'jpeg', 'png'])
