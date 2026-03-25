import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../models';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-item.html'
})
export class ProductItem {
  @Input() product!: Product;

  like() {
    this.product.likes++;
  }
}