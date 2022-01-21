use std::io;

fn processing(domain: String, set: String) {
    
}

fn main() {

    println!("Linear dependency calculator.");

    println!("Wich the domain of vectors? Example: 2, that means R2.");
    let mut domain: String = String::new();
    io::stdin().read_line(&mut domain).expect("Failed to read line");

    println!("Please input the vectors set: ");
    let mut set: String = String::new();
    io::stdin().read_line(&mut set).expect("Failed to read line");

    processing(domain, set);

}