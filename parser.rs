use std::io;

fn split_text(s: &str) -> Vec<String> {
    s.split('>')
        .map(|word| word.to_lowercase())
        .collect()

}


fn main() {
    let mut input = String::new();
    
    println!("Enter command");
    io::stdin().read_line(&mut input).unwrap();
    let rendered = split_text(&input);
    let subject: &String = &rendered[0].clone();
    let verb: &String = &rendered[1].clone();
    let modifier: &Vec<String> = &rendered[2..].to_vec();
    drop(rendered);
    println!("Returned command: {}", modifier.join(" "));
}
