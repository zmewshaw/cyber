undefined8 main(void)

{
    int iVar1;
    int iVar2;
    int iVar3;
    int iVar4;
    int iVar5;
    int iVar6;
    int iVar7;
    int iVar8;
    int iVar9;
    int iVar10;
    int iVar11;
    int iVar12;
    int iVar13;
    int iVar14;
    int iVar15;
    int iVar16;
    int *err_loc;
    char output;

    iVar16 = check_input();
    if (iVar16 == 1) { // Flag
        generate_error_3();
        err_loc = __errno_location();
        iVar16 = *err_loc;

        generate_error_2();
        err_loc = __errno_location();
        iVar1 = *err_loc;

        generate_error_2();
        err_loc = __errno_location();
        iVar2 = *err_loc;

        generate_error_1(); // 
        err_loc = __errno_location();
        iVar3 = *err_loc;

        generate_error_2();
        err_loc = __errno_location();
        iVar4 = *err_loc;

        generate_error_2();
        err_loc = __errno_location();
        iVar5 = *err_loc;

        generate_error_1();
        err_loc = __errno_location();
        iVar6 = *err_loc;

        generate_error_1();
        err_loc = __errno_location();
        iVar7 = *err_loc;

        generate_error_3();
        err_loc = __errno_location();
        iVar8 = *err_loc;

        generate_error_2();
        err_loc = __errno_location();
        iVar9 = *err_loc;

        generate_error_2();
        err_loc = __errno_location();
        iVar10 = *err_loc;

        generate_error_1();
        err_loc = __errno_location();
        iVar11 = *err_loc;

        generate_error_2();
        err_loc = __errno_location();
        iVar12 = *err_loc;

        generate_error_2();
        err_loc = __errno_location();
        iVar13 = *err_loc;

        generate_error_1();
        err_loc = __errno_location();
        iVar14 = *err_loc;

        generate_error_1();
        err_loc = __errno_location();
        iVar15 = *err_loc;

        generate_error_1();
        err_loc = __errno_location();

        output = ((char)iVar1 + (char)iVar2 + (char)iVar3 + (char)iVar4 + (char)iVar5 + (char)iVar6 +
                 (char)iVar7) * (char)iVar16 +
                 ((char)iVar9 + (char)iVar10 + (char)iVar11 +
                 (char)iVar12 + (char)iVar13 + (char)iVar14 + (char)iVar15) * (char)iVar8 +
                 (char)*err_loc;
    }
    else { // Wrong
        output = ((char)iVar1 + (char)iVar2 + (char)*err_loc) * (char)iVar16;
    }