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
    public class QuoteCard  // карточка цитаты
    {
        [Key]
        public Guid IdQuote { get ; set; }
        public string QuoteTitle { get; set; }
        public string QuoteText { get; set; }
        public string QuoteAutor { get; set; }
        public DateTime? DateCreationQuote { get; set; }
        public DateTime? DateUpdateQuote { get; set; }

    }
}
