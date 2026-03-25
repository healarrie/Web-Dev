import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductItem } from '../product-item/product-item';
import { Product } from '../models';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-list.html',
  styleUrls: ['./product-list.css']
})
export class ProductList {
  @Input() products: Product[] = [];
}