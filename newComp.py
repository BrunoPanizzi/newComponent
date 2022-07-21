from sys import argv
from os import scandir, mkdir, getcwd, path



###----FUNCTIONS----###
def get_sub_dirs(directory): 
  return [dir.name for dir in scandir(directory) if dir.is_dir()]

concat = path.join
###-----------------###



###----CONSTANTS----###
COMPONENT_NAME = argv[1]
CWD = getcwd()
###----------------###



###----ASSERTIONS----###
assert len(argv) > 1, 'no component name was provided'


has_src = 'src' in get_sub_dirs(CWD)
assert has_src, 'could not find a `src` subfolder'


has_components = 'components' in get_sub_dirs(concat(CWD, 'src'))
assert has_components, 'could not find a `components` subfolder'


component_exists = COMPONENT_NAME in get_sub_dirs(concat(CWD, 'src', 'components'))
assert not component_exists, f'there is already a `{COMPONENT_NAME}` in the `components` folder'
###------------------###



path = concat(CWD, 'src', 'components', COMPONENT_NAME)

mkdir(path)

# the {{}} is used to escape the {} characters
with open(concat(path, 'index.ts'), 'w', encoding='utf-8') as f:
  f.write(f'export {{ default }} from \'./{COMPONENT_NAME}\'')


with open(concat(path, f'{COMPONENT_NAME}.tsx'), 'w', encoding='utf-8') as f:
  f.write(f'''import {{ Container }} from './styles'

interface props {{}}

export default function {COMPONENT_NAME} ({{}}: props) {{
  return (
    <Container>
      <p>{COMPONENT_NAME}</p>
    </Container>
  )
}}''')

with open(concat(path, 'styles.ts'), 'w', encoding='utf-8') as f:
  f.write(f'''import styled from 'styled-components'

export const Container = styled.div``
''')


print('component created')
