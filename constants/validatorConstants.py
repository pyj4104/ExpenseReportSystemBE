# Type of inputs
TYPEOFINPUT = 'type'
INTEGER = 'integer'
STRING = 'string'
LIST = 'list'

# Properties
ALLOWED = 'allowed' 	# for allowed list
EMPTY = 'empty'			# for empty fields
CASTER = 'coerce'		# casting to other type
REQUIRED = 'required'	# check if required
REGEX = 'regex'			# check uisng regex

# Regexes
REGEXEMAIL = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEXKORNAME = '^[가-힣]{1,4}$'
REGEXLEGALNAME = '^[a-zA-Z,.\'-]+$'