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
    internal class BookCard // карточка книги
    {
        [Key]
        internal Guid IdBook { get ; set; }
        internal string NameBook { get; set; }
        internal string AuthorBook {get; set;}
        internal int PhotoBook { get; set; } // номер фотографии 
        internal string VendorCodeBook { get; set; } // артикул
        internal DateTime RecieptDateBook { get; set; } // дата поступления
        internal string GenreBook { get; set; } // жанр
        internal string DescriptionBook { get; set; }    // описание книги
        internal decimal PriceBook { get; set; } // цена
        internal DateTime DateCreationBook { get; set; } // дата создания книги
        internal  DateTime DateUpdateBook { get; set; } // дата обновления книги


    }
}
