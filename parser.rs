fn split_to_lowercase(s: &str) -> Vec<String> {
    s.split('>')
        .map(|word| word.to_lowercase())
        .collect()
}

fn main() {
let input = "file>upload>return>graph>scatter>prof>stud"; // This is just an example of a user input
let result: Vec<String> = split_to_lowercase(input);
    

let subject = result.get(0).unwrap();
let verb = result.get(1).unwrap();
let modif = result.get(2..).unwrap();

println!("{:?}", subject);
println!("{:?}", verb);
println!("{:?}", modif);
}
