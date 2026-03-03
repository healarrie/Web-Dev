export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  rating: number;
  image: string;
  link: string;
  likes: number;
  categoryId: number;
}

export interface Category {
  id: number;
  name: string;
}

export const categories: Category[] = [
  { id: 1, name: 'Смартфоны' },
  { id: 2, name: 'Ноутбуки' },
  { id: 3, name: 'Часы' },
  { id: 4, name: 'Аксессуары' }
];

export const products: Product[] = [
];