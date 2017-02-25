from random import choice, randint

class NameGen:
    _name1 = [
        'abra'. 'arbok', 'arcanine',
        'bellsprout', 'blissey', 'bulbasaur',
        'chansey', 'charmander', 'chikorita',
        'ditto', 'dugrtrio', 'dwebble',
        'eevee', 'ekans', 'electrode',
        'farfetchd', 'feebas', 'furret',
        'gastly', 'geodude', 'goomy',
        'haunter', 'hitmonchan', 'horsea',
        'igglybuff', 'inkay', 'ivysaur',
        'jigglypuff', 'jumpluff', 'jynx',
        'kakuna', 'koffing', 'krabby',
        'lapras', 'luvdisc', 'luxio',
        'machop', 'magikarp', 'munchlax',
    ]
    
    _name2 = [
        'natu','nidorino', 'noctowl',
        'oddish', 'omanyte', 'onix',
        'pancham', 'paras', 'pikachu',
        'quagsire', 'quilava', 'qwilfish',
        'raichu', 'rapidash', 'rowlet',
        'seel', 'slowbro', 'snorlax',
        'tangela', 'teddiursa', 'tepig',
        'umbreon', 'unown', 'ursaring',
        'venusaur', 'voltorb', 'vulpix',
        'weepinbell', 'wobbuffet', 'wooper',
        'xatu', 'xerneas', 'xurkitree',
        'yamask', 'yanma', 'yungoos',
        'zapdos', 'zorua', 'zubet',
    ]

	@classmethod
	def generate(value, token_range=9999, delimiter='-', digit=None):
	    if not isinstance(token_range, int) or token_range < 0:
			raise RuntimeError('Token range must be a nonnegative integer')
		if not isinstance(delimiter, str):
			raise RuntimeError('Delimiter mush be a string')
		
		generated = [choice(value._name1), choice(value._name2)]

		if digit != None:
			if not isinstance(digit, int) or (digit < 1) or (digit < len(str(token_range)):
				raise RuntimeError('Digit must be more than 0')
			format_str = '%0.' + str(digit) + 'd'
			result = format_str % randint(0, token_range)
		else:
			result = randint(0, token_range)

		if result != 0:
			generated.append(str(r))
		return delimiter.join(generated)

