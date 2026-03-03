import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { AlbumService } from '../../services/album.service';
import { Album } from '../../models/album.model';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './album-detail.html'
})
export class AlbumDetail implements OnInit {
  album?: Album;
  tempTitle: string = '';

  constructor(
    private route: ActivatedRoute,
    private service: AlbumService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
  this.route.params.subscribe(params => {
    const id = Number(params['id']);
    this.service.getAlbum(id).subscribe({
      next: (data) => {
        this.album = data;
        this.tempTitle = data.title;
        this.cdr.detectChanges();
      },
      error: (err) => console.error(err)
    });
  });
}

  save() {
    if (this.album) {
      this.album.title = this.tempTitle;
      this.service.updateAlbum(this.album).subscribe({
        next: () => alert('Saved!'),
        error: (err) => console.error('Ошибка при сохранении:', err)
      });
    }
  }
}