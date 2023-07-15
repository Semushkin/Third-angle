using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Thrid_angle.Database.RestAPI.DTO
{
    [Table("QuoteCard")]
    internal class QuoteCard  // карточка цитаты
    {
        [Key]
        internal Guid IdQuote { get ; set; }
        internal string QuoteTitle { get; set; }
        internal string QuoteText { get; set; }
        internal string QuoteAutor { get; set; }
        internal DateTime DateCreationQuote { get; set; }
        internal DateTime DateUpdateQuote { get; set; }

    }
}
