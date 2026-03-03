import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductList } from './product-list/product-list';
import { ProductService } from './services/productService';
import { Category, Product } from './models';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.html',
  styleUrls: ['./app.css'],
  imports: [CommonModule, ProductList]
})
export class AppComponent implements OnInit {
  categories: Category[] = [];
  selectedCategoryId: number | null = null;
  selectedProducts: Product[] = [];

  constructor(private productService: ProductService) {}

  ngOnInit() {
    this.categories = this.productService.getCategories();
  }

  selectCategory(id: number) {
    this.selectedCategoryId = id;
    this.selectedProducts = this.productService.getProductsByCategory(id);
  }
}