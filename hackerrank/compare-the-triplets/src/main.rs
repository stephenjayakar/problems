use std::io;

fn main() {
    let mut x: u32 = 0;
    let mut y: u32 = 0;
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("asdfkljsldfjds");

    let mut a = Vec::new();
    for num in input.trim().split(' ') {
        a.push(num.parse::<u32>().unwrap());
    }

    input = String::new();
    io::stdin().read_line(&mut input)
        .expect("asdf");

    let mut b = Vec::new();
    for num in input.trim().split(' ') {
        b.push(num.parse::<u32>().unwrap());
    }

    for i in 0..3 {
        if a[i] < b[i] {
            x += 1;
        } else if a[i] > b[i] {
            y += 1;
        }
    }

    println!("{} {}", x, y);
}
