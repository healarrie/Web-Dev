import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Album } from '../../models/album.model';
import { AlbumService } from '../../services/album.service';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './albums.html'
})
export class Albums implements OnInit {
  albums: Album[] = [];

  constructor(
    private service: AlbumService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.load();
  }

  load() {
    this.service.getAlbums().subscribe({
      next: (res) => {
        this.albums = res;
        this.cdr.detectChanges();
      },
      error: (err) => console.error(err)
    });
  }

  delete(id: number, event: Event) {
    event.preventDefault();
    event.stopPropagation();

    this.service.deleteAlbum(id).subscribe({
      next: () => {
        this.albums = this.albums.filter(a => a.id !== id);
        this.cdr.detectChanges();
      }
    });
  }
}