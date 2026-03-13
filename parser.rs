fn split_to_lowercase(s: &str) -> Vec<String> {
    s.split('>')
        .map(|word| word.to_lowercase())
        .collect()
}

fn main() {
    let input = "file>upload>return>graph";
    let result = split_to_lowercase(input);
    println!("{:?}", result);
}
