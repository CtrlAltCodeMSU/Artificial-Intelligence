import java.util.HashMap;

 class Book {
	String author;
	String book;
	double price;
	int publish_year;
	int edition;
	int pages;
	String isbn;

	public Book(String aut, String bk, double p, int year, int pag, int edit, String no) {
		this.author = aut;
		this.book = bk;
		this.price = p;
		this.publish_year = year;
		this.pages = pag;
		this.edition = edit;
		this.isbn = no;
	}

	public String getIsbn() {
		return isbn;
	}

	public String toString() {
		return "Book: " + book + "\nAuthor: " + author + "\nPrice $" + price + "\nPublish Year: " + publish_year + "\nEdition: " + edition +"th"+ "\nPages: " + pages + "\nISBN: " + isbn;
	}
}
class Library{
	private HashMap<String, Book> bookCollection = new HashMap<>();

	public void addBook(Book book){
		bookCollection.put(book.getIsbn(),book);
	}

	public Book findBook(String ISBN) {
		return bookCollection.get(ISBN);
	}
}
public class Main {
	public static void main(String[] args) {
		Library lib =  new Library();
		Book b1 = new Book("Tonny Gaddis" , "C++" , 100 , 2020 , 1250 , 7 , "CS1012" );
		Book b2 = new Book("Bejaurn Straustroup" , "Object First with Java" , 120 , 2012 , 1300 , 9 , "CS1013" );
		Book b3 = new Book("Bejaurn Straustroup" , "Object First with Java" , 120 , 2012 , 1300 , 9 , "CS1014" );
		lib.addBook(b1);
		lib.addBook(b2);
		lib.addBook(b3);

		System.out.println("Search book by ISBN: ");
//		lib.findBook("CS1012");
		System.out.println(lib.findBook("CS1012"));
	}
}



