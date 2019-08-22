
code = '#[cfg(feature = "full")] use serde_derive::{Serialize, Deserialize};\n'
code += '#[cfg(feature = "mini")] use miniserde::{Serialize, Deserialize};\n\n'

for index in range(0, 500):
    code += f'#[derive(Serialize, Deserialize)] pub enum E{index} {{ A, B, C }}\n'

for index in range(0, 500):
    e1 = min(index + 1, 499)
    e2 = index
    code += f'#[derive(Serialize, Deserialize)] pub struct S{index} {{ a: bool, b: i32, c: String, d: E{e1}, e: E{e2} }}\n'

code += 'fn main() {\n'
for index in range(0, 500):
    e1 = min(index + 1, 499)
    e2 = index
    code += f'    let value = S{index} {{ a: true, b: 22, c: "bla".into(), d: E{e1}::A, e: E{e2}::B }};\n'
    code += '    #[cfg(feature = "full")] eprintln!("{}", serde_json::to_string(&value).unwrap());\n'
    code += '    #[cfg(feature = "mini")] eprintln!("{}", miniserde::json::to_string(&value));\n'
code += '}\n'

with open('src/main.rs', 'w') as f:
    f.write(code)


