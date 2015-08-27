{	scopeName = 'source.aa_macro';
	fileTypes = ( );
	patterns = (
		{	name = 'keyword.body.aa_macro';
			begin = '\[';
			end = '[\s|\]]';
			patterns = (
				{	name = 'constant.aa_macro';
					match = '[a-zA-Z0-9]';
				},
			);
		},
		{	name = 'meta.preprocessor.body.aa_macro';
			begin = '\<';
			end = '\>';
		},
		{	name = 'constant.character.escape.body.aa_macro';
			begin = '\{';
			end = '[\s|\}]';
			patterns = (
				{	name = 'string.keyword.aa_macro';
					match = '[a-zA-Z0-9]';
				},
			);
		},
		{	name = 'meta.preprocessor.body.aa_macro';
			begin = '\<';
			end = '\>';
		},
		{	name = 'keyword.bodyc.aa_macro';
			match = '\]';
		},
		{	name = 'constant.character.escape.bodyc.aa_macro';
			match = '\}';
		},
	);
}
