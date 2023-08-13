using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Thrid_angle.Database.RestAPI.Migrations
{
    /// <inheritdoc />
    public partial class NewMigration : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Baskets",
                columns: table => new
                {
                    IdBasket = table.Column<Guid>(type: "TEXT", nullable: false),
                    IdUser = table.Column<Guid>(type: "TEXT", maxLength: 50, nullable: false),
                    IdBook = table.Column<Guid>(type: "TEXT", maxLength: 50, nullable: false),
                    NumberOrderCard = table.Column<Guid>(type: "TEXT", maxLength: 50, nullable: false),
                    StatusOrderCard = table.Column<string>(type: "TEXT", maxLength: 50, nullable: false),
                    NumberCard = table.Column<int>(type: "INTEGER", maxLength: 4, nullable: false),
                    QuantityBooks = table.Column<int>(type: "INTEGER", maxLength: 10, nullable: false),
                    PricePerBook = table.Column<int>(type: "INTEGER", maxLength: 10, nullable: false),
                    DateCreationBasket = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false),
                    DateUbdateBasket = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Baskets", x => x.IdBasket);
                });

            migrationBuilder.CreateTable(
                name: "BookCard",
                columns: table => new
                {
                    IdBook = table.Column<Guid>(type: "TEXT", nullable: false),
                    NameBook = table.Column<string>(type: "TEXT", maxLength: 100, nullable: false),
                    AuthorBook = table.Column<string>(type: "TEXT", maxLength: 100, nullable: false),
                    PhotoBook = table.Column<int>(type: "INTEGER", maxLength: 10, nullable: false),
                    VendorCodeBook = table.Column<string>(type: "TEXT", maxLength: 50, nullable: false),
                    RecieptDateBook = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false),
                    GenreBook = table.Column<string>(type: "TEXT", maxLength: 100, nullable: false),
                    DescriptionBook = table.Column<string>(type: "TEXT", maxLength: 1000, nullable: false),
                    PriceBook = table.Column<decimal>(type: "TEXT", maxLength: 100, nullable: false),
                    DateCreationBook = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false),
                    DateUpdateBook = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_BookCard", x => x.IdBook);
                });

            migrationBuilder.CreateTable(
                name: "OrderCard",
                columns: table => new
                {
                    IdOrder = table.Column<Guid>(type: "TEXT", nullable: false),
                    OrderCardBooksList = table.Column<string>(type: "TEXT", maxLength: 300, nullable: false),
                    DateCreationOrderCard = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false),
                    DateUpdateOrderCard = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false),
                    StatusOrderCard = table.Column<string>(type: "TEXT", maxLength: 100, nullable: false),
                    IdUsers = table.Column<Guid>(type: "TEXT", maxLength: 50, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_OrderCard", x => x.IdOrder);
                });

            migrationBuilder.CreateTable(
                name: "QuoteCard",
                columns: table => new
                {
                    IdQuote = table.Column<Guid>(type: "TEXT", nullable: false),
                    QuoteTitle = table.Column<string>(type: "TEXT", maxLength: 200, nullable: false),
                    QuoteText = table.Column<string>(type: "TEXT", maxLength: 1000, nullable: false),
                    QuoteAutor = table.Column<string>(type: "TEXT", maxLength: 100, nullable: false),
                    DateCreationQuote = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false),
                    DateUpdateQuote = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_QuoteCard", x => x.IdQuote);
                });

            migrationBuilder.CreateTable(
                name: "RequestCard",
                columns: table => new
                {
                    IdRequestCard = table.Column<Guid>(type: "TEXT", nullable: false),
                    CommentTextCard = table.Column<string>(type: "TEXT", maxLength: 500, nullable: false),
                    NumberStars = table.Column<int>(type: "INTEGER", maxLength: 10, nullable: false),
                    IdUser = table.Column<Guid>(type: "TEXT", maxLength: 50, nullable: false),
                    IdBook = table.Column<Guid>(type: "TEXT", maxLength: 50, nullable: false),
                    DateRequestCreation = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false),
                    DateRequestUpdation = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_RequestCard", x => x.IdRequestCard);
                });

            migrationBuilder.CreateTable(
                name: "UserCard",
                columns: table => new
                {
                    IdUser = table.Column<Guid>(type: "TEXT", nullable: false),
                    UserName = table.Column<string>(type: "TEXT", maxLength: 50, nullable: false),
                    SurnameUser = table.Column<string>(type: "TEXT", maxLength: 50, nullable: false),
                    RoleUser = table.Column<string>(type: "TEXT", maxLength: 20, nullable: false),
                    FloorUser = table.Column<string>(type: "TEXT", maxLength: 50, nullable: false),
                    AgeUser = table.Column<int>(type: "INTEGER", maxLength: 100, nullable: false),
                    AddressUser = table.Column<string>(type: "TEXT", maxLength: 100, nullable: false),
                    TelephoneUser = table.Column<string>(type: "TEXT", maxLength: 30, nullable: false),
                    EmailUser = table.Column<string>(type: "TEXT", maxLength: 50, nullable: false),
                    LoginUser = table.Column<string>(type: "TEXT", maxLength: 50, nullable: false),
                    PasswordUser = table.Column<string>(type: "TEXT", maxLength: 50, nullable: false),
                    DateCreationUser = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false),
                    UpdateDateUser = table.Column<DateTime>(type: "TEXT", maxLength: 100, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_UserCard", x => x.IdUser);
                });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Baskets");

            migrationBuilder.DropTable(
                name: "BookCard");

            migrationBuilder.DropTable(
                name: "OrderCard");

            migrationBuilder.DropTable(
                name: "QuoteCard");

            migrationBuilder.DropTable(
                name: "RequestCard");

            migrationBuilder.DropTable(
                name: "UserCard");
        }
    }
}
