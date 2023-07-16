using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Thrid_angle.Database.RestAPI.DTO
{
    [Table("UserCard")]
    internal class UserCard
    {
        [Key]
        internal Guid IdUser { get; set; }
        internal string UserName { get; set; }
        internal string SurnameUser { get; set; }
        internal string FloorUser { get; set; }
        internal int AgeUser { get; set; }
        internal string AddressUser { get; set;}
        internal string TelephoneUser { get; set; }
        internal string EmailUser { get; set; }
        internal string LoginUser { get; set; }
        internal string PasswordUser { get; set; }
        internal DateTime DateCreationUser { get; set; }
        internal DateTime UpdateDateUser { get; set; }
        
    }
   
}
