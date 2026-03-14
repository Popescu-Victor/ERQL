//Not yet integrated into the rest of the project. I'm just experimenting with Rust a bit here to see how much it improves performance on the lower end systems it will ultimately be running.

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
