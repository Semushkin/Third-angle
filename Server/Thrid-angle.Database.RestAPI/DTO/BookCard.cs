using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Thrid_angle.Database.RestAPI.DTO
{

    [Table("BookCard")]
    public class BookCard // карточка книги
    {
        [Key]
        public Guid IdBook { get ; set; }
        public string NameBook { get; set; }
        public string AuthorBook {get; set;}
        public int PhotoBook { get; set; } // номер фотографии 
        public string VendorCodeBook { get; set; } // артикул
        public DateTime RecieptDateBook { get; set; } // дата поступления
        public string GenreBook { get; set; } // жанр
        public string DescriptionBook { get; set; }    // описание книги
        public decimal PriceBook { get; set; } // цена
        public DateTime DateCreationBook { get; set; } // дата создания книги
        public DateTime DateUpdateBook { get; set; } // дата обновления книги


    }
}
